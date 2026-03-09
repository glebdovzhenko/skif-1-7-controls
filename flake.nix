{
  description = "My TANGO DevEnv flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    { self
    , nixpkgs
    , flake-utils
    , ...
    }:
    let
      overlays = [ ];
      systems = [ "x86_64-linux" ];
    in
    flake-utils.lib.eachSystem systems (
      system:
      let
        pkgs = import nixpkgs { inherit overlays system; };
      in
      {
        devShells.default = pkgs.mkShell
          rec {
            name = "tango-dev";
            venvDir = "./.venv";
            nativeBuildInputs = with pkgs; [ 
              mariadb
              tango-cpp 
              tango-database 
              jive
              libz 
              cmake 
              omniorb
              cppzmq
              qt5.qttools.dev
            ];

            buildInputs = with pkgs.python3Packages; [
              python
              venvShellHook
              numpy
              scipy
              pyqt5
              #pyqtwebengine # marked insecure maybe add later
              matplotlib
              pyqtgraph
              qtconsole
              h5py
            ] ++ [pkgs.javaPackages.compiler.openjdk21];

            postVenvCreation = ''
              unset SOURCE_DATE_EPOCH
              pip install --upgrade pip
              pip install pytango
              pip install itango
              pip install sardana
            '';
            postShellHook = ''
              # allow pip to install wheels
              unset SOURCE_DATE_EPOCH
              # setting up project env
              export BASE_DIR=$PWD;
              export PYTHONPATH=$PYTHONPATH":"$PWD;
            '';
            LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.libz}/lib:${pkgs.tango-cpp}/lib:${pkgs.omniorb}";
            CPATH = "${pkgs.tango-cpp}/include/tango";
            QT_QPA_PLATFORM_PLUGIN_PATH = "${pkgs.qt5.qtbase.bin}/lib/qt-${pkgs.qt5.qtbase.version}/plugins";

          };
        devShell = self.devShells.${system}.default;
      }
    );
}
