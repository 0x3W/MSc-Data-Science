import time
import pprint as pp
import networkx as nx

import Network_Based_Recommendation_System_FUNCTIONS as homework_2

################################################################################################################
################################################################################################################
################################################################################################################

print
print("Current time: " + str(time.asctime(time.localtime())))
print
print
print

sum_of_AVEARGE_normalized_DCG_LOWER_BOUND                 = 0.
sum_of_AVEARGE_normalized_DCG_for_PERSONAL_recommendation = 0.

number_of_training_set_test_set_instances = 5
for index in range(1, number_of_training_set_test_set_instances + 1):
    training_set_file = './input_data/u'+str(index)+'_base_homework_format.txt'
    test_set_file     = './input_data/u'+str(index)+'_test_homework_format.txt'
    	
    print
    print
    print ("-----------------------------------------------")
    print ("Current data: ")
    print ("              " + training_set_file)
    print ("              " + test_set_file)
    print
    	
    	
    pp.pprint("Load Test Graph.")
    print ("Current time: " + str(time.asctime(time.localtime())))
    test_graph_users_items = homework_2.create_graph_set_of_users_set_of_items(test_set_file)
    print (" #Users in Test Graph= " + str(len(test_graph_users_items['users'])))
    print (" #Items in Test Graph= " + str(len(test_graph_users_items['items'])))
    print (" #Nodes in Test Graph= " + str(len(test_graph_users_items['graph'])))
    print (" #Edges in Test Graph= " + str(test_graph_users_items['graph'].number_of_edges()))
    print ("Current time: " + str(time.asctime(time.localtime())))
    print
    print
        pp.pprint("Load Training Graph.")
    print ("Current time: " + str(time.asctime(time.localtime())))
    training_graph_users_items = homework_2.create_graph_set_of_users_set_of_items(training_set_file)
    print (" #Users in Training Graph= " + str(len(training_graph_users_items['users'])))
    print (" #Items in Training Graph= " + str(len(training_graph_users_items['items'])))
    print (" #Nodes in Training Graph= " + str(len(training_graph_users_items['graph'])))
    print (" #Edges in Training Graph= " + str(training_graph_users_items['graph'].number_of_edges()))
    print ("Current time: " + str(time.asctime(time.localtime())))
    print
    print
    	
    	
    pp.pprint("Create Item-Item-Weighted Graph.")
    print ("Current time: " + str(time.asctime(time.localtime())))
    item_item_graph = homework_2.create_item_item_graph(training_graph_users_items)
    print (" #Nodes in Item-Item Graph= " + str(len(item_item_graph)))
    print (" #Edges in Item-Item Graph= " + str(item_item_graph.number_of_edges()))
    print ("Current time: " + str(time.asctime(time.localtime())))
    print
    print
    	
    	
    ### Conversion of the 'Item-Item-Graph' to a scipy sparse matrix representation.
    ### This reduces a lot the PageRank running time ;)
    print
    print (" Conversion of the 'Item-Item-Graph' to a scipy sparse matrix representation.")
    N = len(item_item_graph)
    nodelist = item_item_graph.nodes()
    M = nx.to_scipy_sparse_matrix(item_item_graph, nodelist=nodelist, weight='weight', dtype=float)
    print (" Done.")
    print
    #################################################################################################
    
    sum_of_normalizedDCG_for_PERSONAL_recommendation = 0.
    

    	
    	
