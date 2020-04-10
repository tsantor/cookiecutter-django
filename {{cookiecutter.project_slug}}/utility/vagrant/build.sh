#!/usr/bin/env bash

# Builds a manifest shell file by piecing together various files
# included in a Manifest.<ext> (eg - Manifest.mac) file and will
# output a <ext> file.
#
# @author  Tim Santor  <tsantor@xstudios.agency>

# -----------------------------------------------------------------------------
# Include common utils
# -----------------------------------------------------------------------------
source ~/dotfiles/bash/aliases/common/utils.aliases.bash

script_header "Build Manifest"
divline

# -----------------------------------------------------------------------------
# Build Manifest
# -----------------------------------------------------------------------------
for MANIFEST in Manifest.*; do
    FILENAME=$(printf "$MANIFEST" | sed s/Manifest\.//)
    FILENAME=${FILENAME}-vagrant-bootstrap.sh
    rm -f "$FILENAME"

    e_header "Building ${MONOKAI_BLUE}$MANIFEST${RESET} into ${MONOKAI_BLUE}$FILENAME${RESET}"

    while read file; do
        [[ "$file" =~ ^\#.*$ ]] && continue

        #e_include "$file"

        # Append the file to the new file
        cat "$file" >> "$FILENAME" 2> /dev/null || e_warning "File does not exist: ${file}"

        # Add a blank line (for readability)
        echo -e "\n# End:$file\n" >> "$FILENAME"
    done < "$MANIFEST"

    # Make script executable
    chmod u+x $FILENAME

    # Move completed file up a directory
    # mv $FILENAME ..

    e_success "DONE!"
done

# -----------------------------------------------------------------------------
