# Proyecto-entornos CP copy paste
Aqui vamos subiendo las cosas al apartado master

Primero crear una carpeta en el escritorio (con el nombre que querais pero que os acordeis de cual es)
Luego hacerlo abrir VisualSudio, darle a Terminal, nueva Terminal (no hace falta hacerlo con VisualSudio pero a mi personalmente me gusta más)

Primer comando moveros a la carpeta
cd .\Desktop\repositorio\

Luego iniciar git de forma local
git init
Os saldrá este mensaje
Initialized empty Git repository in C:/Users/Ani/Desktop/NombreCarpeta/.git/

Poneis el github (Esto ponerlo tal cual)
git remote add origin https://github.com/aniii-206/Proyecto-entornos-CP-copy-paste-

Mirais el status por si teneis algo sin tener subido en la carpeta
git status
Si no teneis nada en la carpeta os saldrá esto
On branch master

No commits yet

Si teneis algo sin subir os saldrá esto con el archivo sin subir en rojo:
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        interactivo.html
nothing added to commit but untracked files present (use "git add" to track)

Si teneis muchos archivos y solo quereís subir uno:
git add NombreDelArchivo.loQueSea
Si quereis subir todos de una
git add.

Luego haceis un status para comprobar que esta guardado correctamente
No commits yet
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   interactivo.html

Después hacer un commit con un nombre descriptivo para poder identificar si tenemos que volver a esa versión
 git commit -m "Agregue el interactivo.html"
 Os saldrá esto
 [master (root-commit) 911494b] Agregue el interactivo.html
 1 file changed, 11 insertions(+)
 create mode 100644 interactivo.html
On branch master
nothing to commit, working tree clean

Ahora para subir al github hay que hacer un push, la primera vez al no tenerlo identificado os saldrá esto
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.

Esto te da directamente el comando git para que se vaya a nuestro repositorio de github el comando es este
git push --set-upstream origin master
Y os saldrá esto primero

info: please complete authentication in your browser...

Esto te redirige para iniciar sesión con tu cuenta de gihub una vez iniciado sesión continuará con la subida y os saldrá esto en la terminal
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 379 bytes | 379.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/aniii-206/Proyecto-entornos-CP-copy-paste-/pull/new/master
remote: 
To https://github.com/aniii-206/Proyecto-entornos-CP-copy-paste-
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.




No se si mañana viernes o hoy tipo esta noche investigaré como editar algo ya subido :D
