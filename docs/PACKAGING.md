# Packaging notes

v0.1 currently has a preliminary source-tree installer and runit-style wrapper. It is not yet integrated with a verified Venus OS package-manager format.

The included package.sh creates a reviewable source archive when run by the developer. It has not been run. Archive installation layout and service registration must be validated on a test Venus OS unit before this is treated as a package-manager-ready release.

The installer currently assumes a Venus OS runit service directory and the bundled velib_python path. These assumptions need testing.
