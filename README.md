# Proyecto-entornos CP copy paste
Aqui vamos subiendo las cosas al apartado master <br>

Primero crear una carpeta en el escritorio (con el nombre que querais pero que os acordeis de cual es) <br>
Luego hacerlo abrir VisualSudio, darle a Terminal, nueva Terminal (no hace falta hacerlo con VisualSudio pero a mi personalmente me gusta más) <br>

Primer comando moveros a la carpeta <br>
    `cd .\Desktop\repositorio\` <br>

Luego iniciar git de forma local <br>
    `git init` <br>
Os saldrá este mensaje <br>
Initialized empty Git repository in C:/Users/Ani/Desktop/NombreCarpeta/.git/ <br>

Poneis el github (Esto ponerlo tal cual pero con tu nombre de usuario) <br>
    `git remote add origin https://github.com/aniii-206/Proyecto-entornos-CP-copy-paste-` <br>

Mirais el status por si teneis algo sin tener subido en la carpeta <br>
    `git status` <br>
Si no teneis nada en la carpeta os saldrá esto <br>
On branch master <br>

No commits yet <br>

Si teneis algo sin subir os saldrá esto con el archivo sin subir en rojo: <br>
Untracked files: <br>
  (use "git add <file>..." to include in what will be committed) <br>
        interactivo.html <br>
nothing added to commit but untracked files present (use "git add" to track) <br>

Si teneis muchos archivos y solo quereís subir uno: <br>
    `git add NombreDelArchivo.loQueSea` <br>
Si quereis subir todos de una <br>
    `git add .` <br>

Luego haceis un status para comprobar que esta guardado correctamente <br>
No commits yet <br>
Changes to be committed: <br>
  (use "git rm --cached <file>..." to unstage) <br>
        new file:   interactivo.html <br>

Después hacer un commit con un nombre descriptivo para poder identificar si tenemos que volver a esa versión <br>
     `git commit -m "Agregue el interactivo.html"` <br>
 Os saldrá esto <br>
 [master (root-commit) 911494b] Agregue el interactivo.html <br>
 1 file changed, 11 insertions(+) <br>
 create mode 100644 interactivo.html <br>
On branch master <br>
nothing to commit, working tree clean <br>

Ahora para subir al github hay que hacer un push, la primera vez al no tenerlo identificado os saldrá esto <br>
    `git push` <br>
fatal: The current branch master has no upstream branch. <br>
To push the current branch and set the remote as upstream, use <br>

    git push --set-upstream origin master 

To have this happen automatically for branches without a tracking <br>
upstream, see 'push.autoSetupRemote' in 'git help config'. <br>

Esto te da directamente el comando git para que se vaya a nuestro repositorio de github el comando es este <br>
    `git push --set-upstream origin master` <br>
Y os saldrá esto primero <br>

info: please complete authentication in your browser... <br>

Esto te redirige para iniciar sesión con tu cuenta de gihub una vez iniciado sesión continuará con la subida y os saldrá esto en la terminal <br>
Enumerating objects: 3, done. <br>
Counting objects: 100% (3/3), done. <br>
Delta compression using up to 16 threads <br>
Compressing objects: 100% (2/2), done. <br>
Writing objects: 100% (3/3), 379 bytes | 379.00 KiB/s, done. <br>
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0) <br>
remote:  <br>
remote: Create a pull request for 'master' on GitHub by visiting: <br>
remote:      https://github.com/aniii-206/Proyecto-entornos-CP-copy-paste-/pull/new/master <br>
remote: <br>
To https://github.com/aniii-206/Proyecto-entornos-CP-copy-paste- <br>
 * [new branch]      master -> master <br>
branch 'master' set up to track 'origin/master'. <br>




No se si mañana viernes o hoy tipo esta noche investigaré como editar algo ya subido :D :smile:
