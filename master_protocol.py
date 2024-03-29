from globPi import Globpi

class MasterProtocol:

    def __init__(self,piObject: Globpi,id: int):
        self.piObject=piObject            #an instance of the class globpi
        self.id=id

    def prepare_request(self):
        return self.piObject.get_steps()+' '+str(self.id)         #master (server) will send steps and worker id to each worker


    def process_reply(self,the_input):        #master(server) will recieve partial pi of each worker and add it to global pi
        _partialPi=float(the_input)
        self.piObject.addToglobPi(_partialPi)





