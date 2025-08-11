#!/bin/sh

TAG="3.1.0"

git tag -d $TAG
git push origin :$TAG
git tag $TAG
git push origin $TAG
