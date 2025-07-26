# 2. implicitly_wait(10)--> find_element & find_elements---> NSEE wait upto 10s
# implicitly_wait--> default timeout is 0s
# applicable for all FE & FES statements
#
#
# 3. explicit wait
#    WebDriverWait is called explicit wait
#    because we need to specify waiting condition explicitly
#
#
# Feature	                Implicit Wait	                            Explicit Wait
# Scope	                Applied globally to all element searches	    Applied to specific elements or conditions
# Granularity	            One time setting for entire session	        Can specify different waits for different elements
# Conditions	            Waits for presence of element in DOM	    Waits for specific conditions (e.g., visibility, clickability, custom conditions)
# Simplicity	            Easy to set up, minimal configuration	    Requires coding for each wait instance
# Performance	            Can slow down all WebDriver commands if
#                         overused	                                    More targeted, does not slow down unrelated steps
