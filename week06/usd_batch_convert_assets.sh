#!/bin/bash

MAIN_FOLDER="C:/Users/janbo/Documents/Projekty/practice/houdini/td/pipeline-td-course/week06/houdini/avatars"

for SUBFOLDER in "$MAIN_FOLDER"/*; do
    if [ -d "$SUBFOLDER" ]; then   
        echo "Processing $SUBFOLDER"   

        hython week06/usd_utils/usd_conversion_utils.py "C:/Users/janbo/Documents/Projekty/practice/houdini/td/pipeline-td-course/week06/houdini/asset_conversion.hiplc" "$SUBFOLDER"

    fi
done