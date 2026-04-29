Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
# Cleaning up __pycache__ directories