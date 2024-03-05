#IMPORTS#
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class ComplexVisual:
    """
        contains functions which are useful
        for plotting complex functions
    """


    @classmethod
    def modular_plot(cls,F,X,Y,mod_limit=2,color = 'plasma'):
        """
            creates a modular plot
            of the function 
        """

        Z = X + (1j)*Y

        f = F(Z) #applying the mapping#

        phi = np.abs(f)
        alpha = np.angle(f)


        # Normalize alpha for color mapping
        alpha_normalized = (alpha - np.min(alpha)) / (np.max(alpha) - np.min(alpha))

        # Create the 3D surface plot
        fig = go.Figure(data=[go.Surface(
            x = X,
            y = Y,
            z=np.minimum(phi,mod_limit),
            surfacecolor=alpha_normalized, 
            colorscale=color, 
        )])

        fig.update_layout(title='3D Surface Plot with Modulus as Height and Angle as Color',
                        scene=dict(
                            xaxis_title='Re',
                            yaxis_title='Img',
                            zaxis_title=r'f(z)'
                        ))

        # Show the figure
        fig.show()
    
    @classmethod
    def angle_plot(cls,F,X,Y):
        """
            creates an angle plot given the function F
        """


        Z = X + (1j)*Y

        f = F(Z) #applying the mapping#

        alpha1 = np.angle(Z)
        alpha2 = np.angle(f)

        fig = make_subplots(rows=1, cols=2, subplot_titles=('Angle Plot for g(z)=z', 'f(z)'))

        
        fig.add_trace(go.Heatmap(
            z=alpha1,
            x=X[0,:], 
            y=Y[:, 0], 
            colorbar=dict(title='Angle plot of g(z)=z'), 
        ), row=1, col=1)

        fig.add_trace(go.Heatmap(
            z=alpha2,
            x=X[0,:],
            y=Y[:, 0],
            colorbar=dict(title='Angle plot of f(z))'), # Optional: customize the colorbar
        ), row=1, col=2)

        # Update layout if needed
        fig.update_layout(title_text='Side by Side Plots: Angle and Magnitude of f(z)', 
                        xaxis_title='Re', yaxis_title='Img')
    
        # Show the plot
        fig.show()

    @classmethod
    def curve_plot(cls,f,phi,a,b,n_points=1000):
        """
            plots how the function changes given a curve
            parameterised by phi(t), t in [a,b]
        """

        t = np.linspace(a,b,n_points+1)
        x,y = phi(t)

        z = x + (1j)*y

        fz = f(z)

        xnew = np.real(fz)
        ynew = np.imag(fz)

        # Create the plot
        #Create a subplot figure with 1 row and 2 columns
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Plot 1", "Plot 2"))

        # Add the original plot to the first column
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Original Curve'), row=1, col=1)

        # Add the new plot to the second column
        fig.add_trace(go.Scatter(x=xnew, y=ynew, mode='lines', name='New Curve'), row=1, col=2)

        # Update layout if you need to adjust more settings
        #fig.update_layout(height=600, width=800, title_text="Side by Side Subplots")

        # Show the plot
        fig.show()




if __name__ == "__main__":

    f = lambda z: z**2

    x = np.linspace(-1, 1, 100) 
    y = np.linspace(-1, 1, 100) 

    X, Y = np.meshgrid(x, y)

    ComplexVisual.modular_plot(f,X,Y)
 