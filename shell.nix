
# shell.nix
{ pkgs ? import <nixpkgs> {} }:

let

in
  pkgs.mkShell {
    packages = [ 
    pkgs.python3
      pkgs.git
      pkgs.nixfmt
    #   install pip
    pkgs.python3.pkgs.pip
    ];
  }

