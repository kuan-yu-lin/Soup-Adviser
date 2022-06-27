from services.nlu import HandcraftedNLU
from services.bst import HandcraftedBST
from services.policy import HandcraftedPolicy
from services.nlg import HandcraftedNLG

# subtitute of speech module for communicating with the system
from services.hci import ConsoleInput
from services.hci import ConsoleOutput

# domaintrack also work in single domain system
from services.domain_tracker import DomainTracker

from services.service import DialogSystem

from utils.domain.jsonlookupdomain import JSONLookupDomain

domain = JSONLookupDomain('soup')

user_in = ConsoleInput()
user_out = ConsoleOutput()

nlu = HandcraftedNLU(domain=domain)
bst = HandcraftedBST(domain=domain)
policy = HandcraftedPolicy(domain=domain)
nlg = HandcraftedNLG(domain=domain)

d_tracker = DomainTracker(domains=[domain])

ds = DialogSystem(services=[user_in, nlu, bst, policy, nlg, user_out, d_tracker])

if not ds.is_error_free_messaging_pipeline():
    ds.print_inconsistencies()
ds.draw_system_graph(name='soup_chat', show=True)

ds.run_dialog(start_signals={'gen_user_utterance': ''})