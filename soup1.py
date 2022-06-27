from services.service import Service, PublishSubscribe, DialogSystem
from utils.topics import Topic
from utils.domain.jsonlookupdomain import JSONLookupDomain

# inherit from 'Service'
class ServiceA(Service):
    # subscribe to the external signal(start) at the first service
    @PublishSubscribe(sub_topics=['start'])
    def start_system(self, start):
        self.send_message()

    # decorate this method as PublishSubscribe
    # pub_topics=['topic1', 'topic2'] ----> to match the return of method
    @PublishSubscribe(pub_topics=['topic1'])
    def send_message(self):
        # can be {'topic1': 'Hello', 'topic2': 'World'}
        return {'topic1': 'Hello'}

class ServiceB(Service):
    # also want to subscribe to 'topic1', use 'sub_topics=[]'. 
    # what you put in the sub_topics also needs to be as an argument 'def subpub(self, topic1):', it means you received the message from topic1
    @PublishSubscribe(pub_topics=['topic2'], sub_topics=['topic1'])
    def subpub(self, topic1):
        return {'topic2': 'World!'}

class ServiceC(Service):
    # if we want to end after the print, use 'pub_topics=[]'
    @PublishSubscribe(sub_topics=['topic1', 'topic2'], pub_topics=[Topic.DIALOG_END])
    def concatenate(self, topic1, topic2):
        print(f'{topic1} {topic2}')
        # once we have 'pub_topics=', we need to add 'retun sth'
        # if .DIALOG_END is set to False, it will keep running
        # but it can also be the turn indicater if it is set to be False
        return {Topic.DIALOG_END: True}

domain = JSONLookupDomain('soup')

a = ServiceA(domain=domain)
b = ServiceB(domain=domain)
c = ServiceC(domain=domain)

ds = DialogSystem(services=[a, b, c])
# to debug
# if statement: print the information only when there is a bug
if not ds.is_error_free_messaging_pipeline():
    # to check where is the bug
    ds.print_inconsistencies()

# draw a system graph, give it a name ('')
ds.draw_system_graph('soup', show=True)

# run the system
# external signal needed - 'start_signals=', to control when to starts
ds.run_dialog(start_signals={'start/soup': True})

# always remember to end with shutting down the system!!!
ds.shutdown()