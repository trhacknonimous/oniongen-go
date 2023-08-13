{ pkgs }: {
    deps = [
        pkgs.sudo
        pkgs.python39Packages.pip
        pkgs.python39Full
        pkgs.unzip
        pkgs.go_1_17
        pkgs.gopls
    ];
}