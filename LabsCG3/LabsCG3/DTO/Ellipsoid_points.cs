using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LabsCG3.DTO
{
    class Ellipsoid_points
    {
        public static int A = 50;
        public static int B = 100;
        public static int C = 120;
        public double _x, _y, _z;
        public static List<Point3D> Points { get; }

        public void createNewPoint()
        {
            for(int i = 0; i < 100;i++)
            {
                for(int j = 0; j < 120; j++)
                {
                    _x = Ellipsoid.CountingX(i, j);
                    _y = Ellipsoid.CountingY(_x, j);
                    Point3D T = new Point3D(_x, _y, j);
                    Points.Add(T);
                }
            }
        }  
    }
}
