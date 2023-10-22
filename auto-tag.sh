#!/bin/bash

BRANCH_NAME=$(git symbolic-ref --short HEAD)
PREFIX=${BRANCH_NAME%%/*}

if [[ $PREFIX == "release" ]]; then
    TAG="1.0.0"
elif [[ $PREFIX == "feature" ]]; then
    TAG="0.1.0"
elif [[ $PREFIX == "hotfix" ]]; then
    TAG="0.0.1"
else
    TAG="0.0.0"
fi

git tag -a $TAG -m "Automatically generated tag"
git push --tags