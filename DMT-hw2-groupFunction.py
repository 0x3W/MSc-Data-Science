import csv
import time
import pprint as pp
import networkx as nx

import Network_Based_Recommendation_System_FUNCTIONS as homework_2



print
print ("Current time: " + str(time.asctime(time.localtime())))
print
print


all_groups = [
	{1701: 1, 1703: 1, 1705: 1, 1707: 1, 1709: 1}, ### Movie night with friends.
	{1701: 1, 1702: 4}, ### First appointment scenario: the preferences of the girl are 4 times more important than those of the man.
	{1701: 1, 1702: 2, 1703: 1, 1704: 2}, ### Two couples scenario: the preferences of girls are still more important than those of the men...
	{1701: 1, 1702: 1, 1703: 1, 1704: 1, 1705: 1, 1720:10}, ### Movie night with a special guest.
	{1701: 1, 1702: 1, 1703: 1, 1704: 1, 1705: 1, 1720:10, 1721:10, 1722:10}, ### Movie night with 3 special guests.
]
print
pp.pprint(all_groups)
print


graph_file = "./input_data/u_data_homework_format.txt"

pp.pprint("Load Graph.")
print ("Current time: " + str(time.asctime(time.localtime())))
graph_users_items = homework_2.create_graph_set_of_users_set_of_items(graph_file)
print (" #Users in Graph= " + str(len(graph_users_items['users'])))
print (" #Items in Graph= " + str(len(graph_users_items['items'])))
print (" #Nodes in Graph= " + str(len(graph_users_items['graph'])))
print (" #Edges in Graph= " + str(graph_users_items['graph'].number_of_edges()))
print ("Current time: " + str(time.asctime(time.localtime())))
print
print


pp.pprint("Create Item-Item-Weighted Graph.")
print ("Current time: " + str(time.asctime(time.localtime())))
item_item_graph = homework_2.create_item_item_graph(graph_users_items)
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
output_file = open("./Output_Recommendation_for_Group.tsv", 'w')
output_file_csv_writer = csv.writer(output_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)
print
for current_group in all_groups:
    print ("Current group: ")
    pp.pprint(current_group)
    print ("Current time: " + str(time.asctime(time.localtime())))
    	
    sorted_list_of_recommended_items_for_current_group = []
	# Your code here ;)
    listItems = {}
    for current_user1, currentBias in current_group.items():
        print(current_user1,currentBias)
        preference_vector = homework_2.create_preference_vector_for_teleporting(current_user1, graph_users_items)
        personalized_pagerank_vector_of_items = homework_2.pagerank(M, N, nodelist, alpha=0.85, personalization=preference_vector)
        for k, v in personalized_pagerank_vector_of_items.items():
            personalized_pagerank_vector_of_items[k] = v * currentBias
        listItems.update(personalized_pagerank_vector_of_items)
    sorted_list_of_recommended_items_for_current_group = homework_2.create_ranked_list_of_recommended_items(listItems, current_user1, graph_users_items)

    print ("Recommended Sorted List of Items:")
    print(str(sorted_list_of_recommended_items_for_current_group[:30]))
    print
    output_file_csv_writer.writerow(sorted_list_of_recommended_items_for_current_group)
	
output_file.close()	
      

print
print
print ("Current time: " + str(time.asctime(time.localtime())))
print ("Done ;)")
print



