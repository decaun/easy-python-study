from qam.qam_server import QAMServer
qam_server = QAMServer(hostname="localhost",
                       port=5672,
                       username='guest',
                       password='guest',
                       vhost='/',
                       server_id='qamserver')


def adder_function(x, y):
    return x + y


qam_server.register_function(adder_function, 'add')
# it is also possible to register the adder_function as follows:
# qam_server.register_function(adder_function)
# the method-name for registering in this case is adder_function.__name__
qam_server.serve()
