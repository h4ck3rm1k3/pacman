self.description = "Query unneeded deps (installed optdeps required)"

p1 = pmpkg("dummy", "1.0-2")
p1.optdepends = ["dep: for foobar"]
self.addpkg2db("local", p1)

p2 = pmpkg("dep")
p2.reason = 1
self.addpkg2db("local", p2)

self.args = "-Qtd"

self.addrule("PACMAN_RETCODE=1")
self.addrule("!PACMAN_OUTPUT=^dep")