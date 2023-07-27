#!/bin/sh

TAG="3.0.0beta"

git tag -d $TAG
git push origin :$TAG
git tag $TAG
git push origin $TAG
