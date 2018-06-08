#!/bin/bash

[ $# -eq 0 -o $# -gt 3 ] && {
    echo "Usage: deploy_from_github_zip.bash <folder to unzip into> [GitHub-user/repository-name] [branch]"
    exit 1
}

project=$1
repo=${2-LSSTDESC/start_paper}
branch=${3-deploy}

[ -e $project ] && {
    echo "$project/ already exists! If you want to possibly overwrite things in this folder, press enter; otherwise, this is your opportunity to Crtl-C."
    read
    #exit 2
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
    mkdir -p $wd/$project && \
    mv -v $dir/* $wd/$project/ && \
    cd $wd && \
    rm -rf $tmpdir
