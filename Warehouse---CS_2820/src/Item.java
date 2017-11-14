import java.awt.Point;

// Leon Grund
public class Item {
	private boolean bin;
	private boolean packag;
	private int ID;
	private int x,y;
	private String progress;
	
	public Item(int item, int id){
		if(item == 0){bin = true;}
		if(item == 1){packag = true;}
		//ID = id;
	}
	
	//setters
	public void setID(int id){ID = id;}
	public void updateLocation(int x,int y){
		this.x = x;
		this.y = y;
	}
	public void setProgress(String prg){progress = prg;}
	public Point Location(){return null;}
	//getters
	public int getID(){return ID;}
	public int[] getLocation(){return new int[] {x,y};}
	public String getProgess(){return progress;}
	public void setLocation(Point p){;}
}
