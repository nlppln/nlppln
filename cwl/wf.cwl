{
    "cwlVersion": "v1.0", 
    "$graph": [
        {
            "class": "Workflow", 
            "inputs": [
                {
                    "type": "Directory", 
                    "id": "#main/in_dir"
                }, 
                {
                    "type": "string", 
                    "id": "#main/out_file"
                }, 
                {
                    "type": [
                        "null", 
                        {
                            "type": "array", 
                            "items": "int"
                        }
                    ], 
                    "id": "#main/test"
                }, 
                {
                    "type": "boolean", 
                    "id": "#main/testb"
                }, 
                {
                    "type": "float", 
                    "id": "#main/testf"
                }
            ], 
            "outputs": [
                {
                    "type": "File", 
                    "outputSource": "#main/basic-text-statistics/metadata_out", 
                    "id": "#main/stats"
                }
            ], 
            "steps": [
                {
                    "run": "#basic-text-statistics.cwl", 
                    "in": [
                        {
                            "source": "#main/pattern-nl/out_files", 
                            "id": "#main/basic-text-statistics/in_files"
                        }, 
                        {
                            "source": "#main/out_file", 
                            "id": "#main/basic-text-statistics/out_file"
                        }
                    ], 
                    "out": [
                        "#main/basic-text-statistics/metadata_out"
                    ], 
                    "id": "#main/basic-text-statistics"
                }, 
                {
                    "run": "#ls.cwl", 
                    "in": [
                        {
                            "source": "#main/in_dir", 
                            "id": "#main/ls/in_dir"
                        }
                    ], 
                    "out": [
                        "#main/ls/out_files"
                    ], 
                    "id": "#main/ls"
                }, 
                {
                    "run": "#pattern-nl.cwl", 
                    "in": [
                        {
                            "source": "#main/ls/out_files", 
                            "id": "#main/pattern-nl/in_files"
                        }
                    ], 
                    "out": [
                        "#main/pattern-nl/out_files"
                    ], 
                    "id": "#main/pattern-nl"
                }
            ], 
            "id": "#main"
        }, 
        {
            "class": "CommandLineTool", 
            "baseCommand": [
                "python", 
                "-m", 
                "nlppln.commands.basic_text_statistics"
            ], 
            "inputs": [
                {
                    "type": {
                        "type": "array", 
                        "items": "File"
                    }, 
                    "inputBinding": {
                        "position": 2
                    }, 
                    "id": "#basic-text-statistics.cwl/in_files"
                }, 
                {
                    "type": "string", 
                    "inputBinding": {
                        "position": 3
                    }, 
                    "id": "#basic-text-statistics.cwl/out_file"
                }
            ], 
            "outputs": [
                {
                    "type": "File", 
                    "outputBinding": {
                        "glob": "$(inputs.out_file)"
                    }, 
                    "id": "#basic-text-statistics.cwl/metadata_out"
                }
            ], 
            "id": "#basic-text-statistics.cwl"
        }, 
        {
            "class": "CommandLineTool", 
            "baseCommand": [
                "python", 
                "-m", 
                "nlppln.commands.ls"
            ], 
            "inputs": [
                {
                    "type": "Directory", 
                    "inputBinding": {
                        "position": 2
                    }, 
                    "id": "#ls.cwl/in_dir"
                }, 
                {
                    "type": [
                        "null", 
                        "boolean"
                    ], 
                    "inputBinding": {
                        "prefix": "--recursive"
                    }, 
                    "id": "#ls.cwl/recursive"
                }
            ], 
            "stdout": "cwl.output.json", 
            "outputs": [
                {
                    "type": {
                        "type": "array", 
                        "items": "File"
                    }, 
                    "id": "#ls.cwl/out_files"
                }
            ], 
            "id": "#ls.cwl"
        }, 
        {
            "class": "CommandLineTool", 
            "baseCommand": [
                "python", 
                "-m", 
                "nlppln.commands.pattern_nl"
            ], 
            "inputs": [
                {
                    "type": {
                        "type": "array", 
                        "items": "File"
                    }, 
                    "inputBinding": {
                        "position": 2
                    }, 
                    "id": "#pattern-nl.cwl/in_files"
                }, 
                {
                    "type": [
                        "null", 
                        "Directory"
                    ], 
                    "inputBinding": {
                        "prefix": "--out_dir=", 
                        "separate": false
                    }, 
                    "id": "#pattern-nl.cwl/out_dir"
                }
            ], 
            "outputs": [
                {
                    "type": {
                        "type": "array", 
                        "items": "File"
                    }, 
                    "outputBinding": {
                        "glob": "*.json"
                    }, 
                    "id": "#pattern-nl.cwl/out_files"
                }
            ], 
            "id": "#pattern-nl.cwl"
        }
    ]
}