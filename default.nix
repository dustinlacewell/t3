with import <nixpkgs> {};

# with import ./deps.nix;

with python3Packages;

buildPythonApplication {
  pname = "t3";
  version = "0.1.0";
  propagatedBuildInputs = [ lxml jinja2 click ];
  src = ./.;
  # src = fetchFromGitHub {
    #   owner = "dustinlacewell";
    #   repo = "t3sketch";
    #   rev = "71d20cb6df561c4f63e059841fa9487cb2f2777f";
    #   sha256 = "1lrv5l2r5wsbvcx6l0679z1ds3kil7szp52ni4x2kc4qbx26n1rr";
    # };
}
