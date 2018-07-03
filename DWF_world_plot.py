import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def make_DWF_globe(observatories, outdir, max_angle=10, step_size=1):
    """ Creates images (pngs) of the globe with the 
    locations of DWF observatories. These can be combined
    into a fancy movie.
    
    Parameters
    ----------
    
    observatories : dictionary
        The dictionary of observatories with coords, 
        colours and markers.
        
        e.g {"MeerKAT" : [(21.444819, -30.712176), "red", "D"]}
        
    outdir : string
        The output directory for the images
        
    max_angle : integer
        The total angle of rotation in degrees for the final plot 
    
    step_size : float or integer
        The angular size in degrees between each frame
    
    """
    
    # Coordinate, Colour and Marker indexes in the dictionary
    cood_idx = 0
    colr_idx = 1
    mark_idx = 2

    # The x, y offsets for the Observatory labels
    labx_offset = 2
    laby_offset = 2

    # Number of frames to make
    num_frames = int(max_angle / step_size)

    for i in range(num_frames):
        plt.figure(figsize=(8, 6), dpi=200)
        
        # m is the map Basemap oject
        m = Basemap(projection="ortho", lat_0=0, lon_0=step_size*i)
        
        # Use bluemarble background
        # Can also use m.shadedrelief() for a more atlas feel
        m.bluemarble()

        for label in observatories.keys():
            # Get x, y corrds from dictionary and convert them to map coords
            x, y = m(observatories[label][cood_idx][0], observatories[label][cood_idx][1])
            
            # Plot Observatories using markers and colours from dictionary
            m.scatter(x, y, marker=observatories[label][mark_idx], color=observatories[label][colr_idx])
        
            # Create Observatory label positions
            labx, laby = m(observatories[label][cood_idx][0] + labx_offset, 
                           observatories[label][cood_idx][1] + laby_offset)
            # Plot labels
            plt.annotate(label, xy=(labx, laby), color='white')


        plt.savefig("{0}/DWF_globe_plot_{1:03}".format(outdir, i),
                    transparent=True)
        plt.clf()
    print("COMPLETE")

if __name__ == "__main__":
    outdir = "/Users/abatten/saraplots"

    observatories = {"MeerKAT" : [(21.444819, -30.712176), "red", "D"],
                     "MWA" : [(116.670866, -26.702681), "green", "o"],
                     "VIRGO" : [(10.505021, 43.631456), "magenta", "x"],
                     "Etelman" : [(-64.956400, 18.352395), "cyan", "o"],
                     "LIGO-LA" : [(-90.772039, 30.564180), "cyan", "x"]
                    }

    make_DWF_globe(observatories, outdir, max_angle=360, step_size=10)
