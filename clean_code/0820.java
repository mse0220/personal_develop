//anti parten
public class Point
{
    protected int x;
    protected int y;

    public Point(){}

    public void setX(int x)
    {
        this.x = x;
    }
    public void setY(int y)
    {
        this.y = y;
    }

}

public class Point{
    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Main {
    public static void main(String[] args) {
        Point location = new Point();

        location.setX(1);
        location.setY(2);

        System.out.println("x: " + location.getX());
        System.out.println("y: " + location.getY());
    }
}



