from invoke import task, run

@task
def pdf(c):
    """
    Tarea que genera la documentación del proyecto en formato pdf
    """
    print("Generando documentación...")
    run("./scripts/pdf.sh", shell="/bin/sh")

@task
def clean(c):
    """
    Tarea para limpiar los archivos intermedios generados por latex
    """
    print("Limpiando archivos...")
    run("rm -f doc/*.aux doc/*.bbl doc/*.bcf doc/*.blg doc/*.log doc/*.out doc/*.run.xml doc/*.toc doc/*.lof doc/*.ist doc/*.idx doc/*.glsdefs doc/*.glo doc/*.ilg doc/*.ind doc/*.gls doc/*.glg", shell="/bin/sh")
