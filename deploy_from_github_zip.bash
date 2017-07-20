#!/bin/bash

[ $# -eq 0 -o $# -gt 3 ] && {
    echo "Usage: deploy_from_github_zip.bash <new project name> [GitHub-user/repository-name] [branch]"
    exit 1
}

project=$1
repo=${2-LSSTDESC/start_paper}
branch=${3-master}

[ -e $project ] && {
    echo "$project already exists; aborting"
    exit 2
}

url=https://github.com/$repo/archive/$branch.zip
dir=$(echo $url | cut -f5 -d/)-$branch
zipfile=$branch.zip
tmpdir=$(mktemp -d)
wd=$(pwd)

wget -O $tmpdir/$zipfile $url && \
    cd $tmpdir && \
    unzip $zipfile && \
    rm -fv $zipfile && \
    mv -v $dir $wd/$project && \
    cd $wd && rmdir $tmpdir
