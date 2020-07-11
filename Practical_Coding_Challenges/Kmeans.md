Coding out Kmeans from scratch
![](https://codesignal.s3.amazonaws.com/uploads/1594152883028/download.gif)

Step 0 - Generate the 2D dataset
# Put in any data, or use Amber's function.
# Note Amber's method only works with 2D data, so you can use a random generator instead for higher dimensionality.
* self.data = np.random.normal(size=(n_data, dim))

Step 1 - Pick K random points as cluster centers called centroids.
Step 2 - Assign each x to the nearest cluster by calculating its distance to each centroid (start with Euclidean).
Step 3 - Find the new cluster center by taking the average of the assigned points.
Step 4 - Repeat Step 2 and 3 for a given number of iterations until none of the cluster assignments change.
Step 5 - Using the elbow method, determine the optimal number of clusters for k-means clustering
 ![](https://codesignal.s3.amazonaws.com/uploads/1594154277600/distortion1.png)
 [Plotting tips](https://www.geeksforgeeks.org/elbow-method-for-optimal-value-of-k-in-kmeans/)

Step 6 - Compare this to KMEANS from scikit learn
Step 7 (optional) - Use batches!

Note:
I wanted to post a possible Python pitfall that’s come up twice this week and can be super-confusing to debug.  When initializing a list of empty lists (e.g. for cluster assignments in k-means), do this:

my_list = [[] for i in range(num_lists)]
my_list[0].append(‘item_for_list_0'’) yields [[‘item_for_list_0’],[],[],[],[]], which is typically what you want

Do not do this:
my_list = [[]] * num_lists
because my_list[0].append(‘ item_for_list_0’) yields [[‘item_for_list_0’],[‘item_for_list_0’],[‘item_for_list_0’],[‘item_for_list_0’],[‘item_for_list_0’]]

In the latter case, every list element is a reference to the same list.  So please be careful!
