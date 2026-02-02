// HolyC Graphics Demo
// TempleOS has built-in 640x480 16-color graphics

U0 DrawDemo() {
    // Clear screen
    GrRect(gr.dc, 0, 0, GR_WIDTH, GR_HEIGHT, BLACK);
    
    // Draw rectangle
    GrRect(gr.dc, 100, 100, 200, 150, RED);
    
    // Draw line
    GrLine(gr.dc, 0, 0, 640, 480, GREEN);
    
    // Draw text
    GrPrint(gr.dc, 200, 50, "NullSec HolyC!");
    
    // Wait for keypress
    GetChar;
}

DrawDemo;
