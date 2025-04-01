import os
import hou
import voptoolutils

def convert_asset():
    assets_dir = "C:/Users/janbo/Documents/Projekty/practice/houdini/td/pipeline-td-course/week06/houdini/avatars"

    obj_node = hou.node("/stage/").createNode("objnet", "load_avatars")

    for file in os.listdir(assets_dir):
        # if file.endswith(".glb"):
        if file.endswith("A.glb"):
            # asset name
            asset_name = file[:-4]

            # load gltf and unpack
            gltf_node = obj_node.createNode("gltf_hierarchy",asset_name)
            gltf_node.parm("filename").set(os.path.join(assets_dir, file))
            gltf_node.parm("assetfolder").set(os.path.join(assets_dir, asset_name))
            gltf_node.parm("buildscene").pressButton()
            
            gltf_mats = gltf_node.node("materials").children()
            
            # create usd prim
            prim_lop = hou.node("/stage/").createNode("primitive", asset_name)
            prim_lop.parm("primkind").set("component")

            # import asset
            sop_create = hou.node("/stage/").createNode("sopcreate")
            sop_inside = sop_create.node("sopnet/create/")
            # process sops
            obj_merge = sop_inside.createNode("object_merge")
            obj_merge.parm("objpath1").set(f"/stage/load_avatars/{asset_name}/*")
            blast = obj_merge.createOutputNode("blast")
            blast.parm("group").set('@name==""')
            blast.parm("grouptype").set(4)
            attr_wrangle = blast.createOutputNode("attribwrangle")
            attr_wrangle.parm("class").set(1)
            attr_wrangle.parm("snippet").set("s@path = '/' + split(s@shop_materialpath, '/')[-1];")
            output_sop = attr_wrangle.createOutputNode("output")

            # graft stages
            graft_lop = prim_lop.createOutputNode("graftstages")
            graft_lop.parm("destpath").set("/geo")
            graft_lop.parm("primkind").set("subcomponent")
            graft_lop.setNextInput(sop_create)

            # materials
            mat_lop = graft_lop.createOutputNode("materiallibrary")
            # create materials from source
            for mat in gltf_mats:
                # create  material builder
                mat_builder = None
                name = mat.name()
                mask = voptoolutils.KARMAMTLX_TAB_MASK
                folder_label= 'Karma Material Builder'
                render_context = "kma"
                mat_builder = voptoolutils._setupMtlXBuilderSubnet(subnet_node=mat_builder, destination_node=mat_lop, name=name, mask=mask, folder_label=folder_label, render_context=render_context)

                shader = mat_builder.node("mtlxstandard_surface")

                # bcl
                if mat.parm("basecolor_useTexture").eval() == True:
                    tex = mat_builder.createNode("mtlximage", "bcl")
                    tex.parm("file").set(mat.parm("basecolor_texture").eval())
                    tex_out_idx = tex.outputIndex("out")
                    shader_in_idx = shader.inputIndex("base_color")
                    shader.setInput(shader_in_idx, tex, tex_out_idx)
                # spr
                if mat.parm("rough_useTexture").eval() == True:
                    tex = mat_builder.createNode("mtlximage", "spr")
                    tex.parm("file").set(mat.parm("rough_texture").eval())
                    tex_out_idx = tex.outputIndex("out")
                    shader_in_idx = shader.inputIndex("specular_roughness")
                    shader.setInput(shader_in_idx, tex, tex_out_idx)
                # nrm
                if mat.parm("baseBumpAndNormal_enable").eval() == True:
                    tex = mat_builder.createNode("mtlximage", "nrm")
                    tex.parm("file").set(mat.parm("baseNormal_texture").eval())
                    tex_out_idx = tex.outputIndex("out")
                    shader_in_idx = shader.inputIndex("normal")
                    shader.setInput(shader_in_idx, tex, tex_out_idx)
            # assigne materials
            mat_lop.parm("materials").set(len(mat_lop.children()))
            for idx, mat in enumerate(mat_lop.children()):
                mat_name = mat.name()
                mat_lop.parm(f"matnode{idx+1}").set(mat_name)
                mat_lop.parm(f"matpath{idx+1}").set(f"/{asset_name}/materials/{mat_name}")
                mat_lop.parm(f"assign{idx+1}").set(True)
                mat_lop.parm(f"geopath{idx+1}").set(f"/{asset_name}/geo/{mat_name}")
            
            # create rops
            usd_rop_lop = mat_lop.createOutputNode("usd_rop")
            usd_rop_lop.parm("lopoutput").set(os.path.join(assets_dir, "usd", f"{asset_name}.usd"))

            print(f"Asset < {asset_name} > ready for conversion!")

    # obj_node.destroy()