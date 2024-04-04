#!/usr/bin/env bash

# @author  Tim Santor  <tsantor@xstudios.agency>

# -----------------------------------------------------------------------------
# Include common utils
# -----------------------------------------------------------------------------
source ~/dotfiles/bash/aliases/common/utils.aliases.bash

# -----------------------------------------------------------------------------
XSTUDIOS_BITBUCKET="/Users/tsantor/Sandbox/BitBucket Pages/xstudios.bitbucket.org"
CURRENT_DIR=`pwd`
DOCKER_CONTAINER={{cookiecutter.project_slug}_mkdocs
TARGET_DIR={{cookiecutter.project_slug}

e_header "Building docs..."
# mkdocs build --clean
docker exec -it $DOCKER_CONTAINER mkdocs build --clean

divline
e_header "Moving latest HTML files to Bitbucket pages project repo..."
rm -rf "${XSTUDIOS_BITBUCKET}/${TARGET_DIR}"

divline
e_header "Pull latest and move site files into repo ..."
cd "${XSTUDIOS_BITBUCKET}"
git pull
sudo mv -fv "${CURRENT_DIR}/site" "${XSTUDIOS_BITBUCKET}/${TARGET_DIR}"

divline
e_header "Committing latest files to Bitbucket..."

git add -A
git commit -m 'updated docs'
git push

cd - > /dev/null 2>&1

divline
e_success "DONE!"
