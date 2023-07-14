# will contain blueprint of the endpoints and path

from flask import Blueprint
from flask_restful import Api
from Server.Views.customerviews import GetAllCustomers,AddCustomer,CustomerResourcesById
from Server.Views.transactionviews import GetAllTransactions,AddTransaction,TransactionResource


Version_one = Blueprint('auth', __name__, url_prefix='/api/v1')
api = Api(Version_one)

# all path endpoints
# customer paths 
api.add_resource(GetAllCustomers, '/customers', endpoint= 'customer')
api.add_resource(AddCustomer, '/customers')
api.add_resource(CustomerResourcesById, '/customers/<int:customer_id>')

#Transactions endpoints

api.add_resource(GetAllTransactions, '/transactions')
api.add_resource(AddTransaction, '/transactions')
api.add_resource(TransactionResource, '/transactions/<int:transaction_id>')