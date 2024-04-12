import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        List<Point> points = new ArrayList<>();
        for (int i = 0; i < line.length; i++) {
            for (int j = i + 1; j < line.length; j++) {
                Point intersection = getIntersection(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2]);
                if (intersection != null) {
                    points.add(intersection);
                }
            }
        }
        
        long maxX = Long.MIN_VALUE;
        long maxY = Long.MIN_VALUE; 
        long minX = Long.MAX_VALUE;
        long minY = Long.MAX_VALUE;
        
        for (int i = 0; i < points.size(); i++) {
            maxX = Math.max(maxX, points.get(i).x);
            maxY = Math.max(maxY, points.get(i).y);
            minX = Math.min(minX, points.get(i).x);
            minY = Math.min(minY, points.get(i).y);
        }
        
        int xLength = (int)(maxX - minX + 1);
        int yLength = (int)(maxY - minY + 1);
        char board[][] = new char[yLength][xLength];
        
        for (int i = 0; i < yLength; i++) {
            for (int j = 0; j < xLength; j++) {
                board[i][j] = '.';
            }
        }
        
        for (int i = 0; i < points.size(); i++) {
            int x = (int)(points.get(i).x - minX);
            int y = (int)(maxY - points.get(i).y);
            board[y][x] = '*';
        }
        
        String[] answer = new String[board.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = new String(board[i]);
        }
        return answer;
    }
    
    public static Point getIntersection(long a, long b, long e, long c, long d, long f) {
        double x = (double)(b*f - e*d) / (a*d - b*c);
        double y = (double)(e*c - a*f) / (a*d - b*c);
        
        if ((x % 1 != 0) || (y % 1 != 0)) {
            return null;
        }
        return new Point((long)x, (long)y);
    }
    
    private static class Point {
        public final long x, y;
        private Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }
}