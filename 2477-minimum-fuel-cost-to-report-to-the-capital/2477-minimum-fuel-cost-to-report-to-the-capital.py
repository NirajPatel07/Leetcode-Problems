from collections import defaultdict

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # Create a dictionary to store the edges in the graph
        graph = defaultdict(list)
        for city_1, city_2 in roads:
            graph[city_1].append(city_2)
            graph[city_2].append(city_1)
        
        # Initialize the minimum fuel cost to 0
        minimum_fuel_cost = 0
        # Create a set to store the cities that have been visited
        visited_cities = set()
        
        # Define a helper function to traverse the graph
        def dfs(city):
            nonlocal minimum_fuel_cost
            # If the city has already been visited, return 0
            if city in visited_cities: return 0
            # Mark the city as visited
            visited_cities.add(city)
            # Initialize a variable to store the number of representatives in this city
            representatives = 0
            # Loop through the cities connected to this city
            for connected_city in graph[city]:
                # Recursively call the dfs function to count the number of representatives in the connected city
                connected_city_representatives = dfs(connected_city)
                # Calculate the number of cars needed to transport all the representatives in the connected city
                minimum_fuel_cost += (connected_city_representatives + seats - 1) // seats
                # Add the number of representatives in the connected city to the representatives variable
                representatives += connected_city_representatives
            # Return the number of representatives in this city, plus the representative from this city
            return representatives + 1
        
        # Call the dfs function starting from city 0 (the capital city)
        dfs(0)
        # Return the minimum fuel cost
        return minimum_fuel_cost
