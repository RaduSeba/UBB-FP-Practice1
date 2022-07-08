from domain.validators import EvenimentValidator,PersoanaValidator
from repository.eveniment_repo import EvenimentRepoFile,PersoanaRepoFile
from service.organizare_service import PersoanaService,EvenimentService
from ui.consola import Conslola


val_persoana=PersoanaValidator()
repo_persoana_file=PersoanaRepoFile("data/persoana.txt")
srv_persoana=PersoanaService(repo_persoana_file,val_persoana)

val_eveniment=EvenimentValidator()
repo_eveniment_file=EvenimentRepoFile("data/eveniment.txt")
srv_eveniment=EvenimentService(repo_eveniment_file,val_eveniment)

ui=Conslola(srv_persoana,srv_eveniment)
ui.show_ui()