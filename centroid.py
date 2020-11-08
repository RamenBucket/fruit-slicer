def find_centroid(v): 
    ans = [0, 0] 
  
    n = len(v) 
    signedArea = 0
  
    # For all vertices 
    for i in range(len(v)): 
  
        x0 = v[i][0] 
        y0 = v[i][1] 
        x1 = v[(i + 1) % n][0] 
        y1 =v[(i + 1) % n][1] 
  
        # Calculate value of A 
        # using shoelace formula 
        A = (x0 * y1) - (x1 * y0) 
        signedArea += A 
  
        # Calculating coordinates of 
        # centroid of polygon 
        ans[0] += (x0 + x1) * A 
        ans[1] += (y0 + y1) * A 
  
    signedArea *= 0.5
    ans[0] = (ans[0]) / (6 * signedArea) 
    ans[1] = (ans[1]) / (6 * signedArea) 
  
    return ans 



def testCentroid():
    vp = [ [ 1, 2 ], 
        [ 3, -4 ], 
        [ 6, -7 ] ] 
    
    ans = find_centroid(vp) 
    
    print(round(ans[0], 12), ans[1]) 

testCentroid()