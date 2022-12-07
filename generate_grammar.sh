#!/bin/bash
java -jar "./lib/antlr3.jar" "./grammars/AST.g"  -o "./src"
mv ./src/grammars/* ./src
rmdir ./src/grammars