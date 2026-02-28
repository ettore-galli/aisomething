vscode="/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"

PATTERN='python|pylance|jupyter|pyright|ms-python|ms-toolsai'
EXTENSIONS=$("${vscode}" --list-extensions | grep -Ei 'python|pylance|jupyter|pyright' || true)

echo $EXTENSIONS

for ext in $EXTENSIONS; do
    echo "Disinstallo: $ext"
    echo 
    echo "${vscode}" --uninstall-extension "$ext" || true
    echo 

done

ext_home="$HOME/.vscode/extensions" 

# ls -latr1 "${ext_home}" | grep -Ei 'python|pylance|jupyter|pyright' || true

"${vscode}" --uninstall-extension ms-toolsai.jupyter-keymap-1.1.2 || true
"${vscode}" --uninstall-extension ms-toolsai.vscode-jupyter-slideshow-0.1.6 || true
"${vscode}" --uninstall-extension ms-toolsai.vscode-jupyter-cell-tags-0.1.9 || true
"${vscode}" --uninstall-extension ms-python.black-formatter-2025.2.0 || true
"${vscode}" --uninstall-extension ms-python.autopep8-2025.2.0 || true
"${vscode}" --uninstall-extension ms-python.isort-2025.0.0 || true
"${vscode}" --uninstall-extension ms-toolsai.jupyter-renderers-1.3.0 || true
"${vscode}" --uninstall-extension ms-toolsai.jupyter-2025.9.1-darwin-arm64 || true
"${vscode}" --uninstall-extension ms-python.vscode-pylance-2025.10.4 || true
"${vscode}" --uninstall-extension ms-python.debugpy-2025.18.0-darwin-arm64 || true
"${vscode}" --uninstall-extension ms-python.python-2026.2.0-darwin-arm64 || true
"${vscode}" --uninstall-extension ms-python.vscode-pylance-2026.1.1 || true
"${vscode}" --uninstall-extension ms-python.vscode-python-envs-1.20.1-darwin-arm64 || true
 
rm -rf "${ext_home}/ms-toolsai.jupyter-keymap-1.1.2" || true
rm -rf "${ext_home}/ms-toolsai.vscode-jupyter-slideshow-0.1.6" || true
rm -rf "${ext_home}/ms-toolsai.vscode-jupyter-cell-tags-0.1.9" || true
rm -rf "${ext_home}/ms-python.black-formatter-2025.2.0" || true
rm -rf "${ext_home}/ms-python.autopep8-2025.2.0" || true
rm -rf "${ext_home}/ms-python.isort-2025.0.0" || true
rm -rf "${ext_home}/ms-toolsai.jupyter-renderers-1.3.0" || true
rm -rf "${ext_home}/ms-toolsai.jupyter-2025.9.1-darwin-arm64" || true
rm -rf "${ext_home}/ms-python.vscode-pylance-2025.10.4" || true
rm -rf "${ext_home}/ms-python.debugpy-2025.18.0-darwin-arm64" || true
rm -rf "${ext_home}/ms-python.python-2026.2.0-darwin-arm64" || true
rm -rf "${ext_home}/ms-python.vscode-pylance-2026.1.1" || true
rm -rf "${ext_home}/ms-python.vscode-python-envs-1.20.1-darwin-arm64" || true


# "${vscode}" --install-extension ms-toolsai.jupyter-keymap ms-toolsai.vscode-jupyter-slideshow ms-toolsai.vscode-jupyter-cell-tags ms-python.black-formatter ms-python.autopep8 ms-python.isort ms-toolsai.jupyter-renderers ms-toolsai.jupyter ms-python.vscode-pylance ms-python.debugpy ms-python.python ms-python.vscode-python-envs

"${vscode}" --install-extension ms-toolsai.jupyter-keymap
"${vscode}" --install-extension ms-toolsai.vscode-jupyter-slideshow
"${vscode}" --install-extension ms-toolsai.vscode-jupyter-cell-tags
"${vscode}" --install-extension ms-python.black-formatter
"${vscode}" --install-extension ms-python.autopep8
"${vscode}" --install-extension ms-python.isort
"${vscode}" --install-extension ms-toolsai.jupyter-renderers
"${vscode}" --install-extension ms-toolsai.jupyter
"${vscode}" --install-extension ms-python.vscode-pylance
"${vscode}" --install-extension ms-python.debugpy
"${vscode}" --install-extension ms-python.python
"${vscode}" --install-extension ms-python.vscode-python-envs