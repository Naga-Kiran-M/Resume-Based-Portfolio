/* Real-Time Heartbeat Monitoring System using PIC16F876 */
#include <xc.h>
#define _XTAL_FREQ 4000000  // Define system frequency

// Configuration Bits
#pragma config FOSC = XT      // External Oscillator
#pragma config WDTE = OFF     // Watchdog Timer disabled
#pragma config PWRTE = OFF    // Power-up Timer disabled
#pragma config BOREN = ON     // Brown-out Reset enabled
#pragma config LVP = OFF      // Low Voltage Programming disabled

// Define LCD Pins
#define RS RB0
#define EN RB1
#define D4 RB2
#define D5 RB3
#define D6 RB4
#define D7 RB5

void LCD_Command(unsigned char cmd);
void LCD_Char(unsigned char data);
void LCD_Init();
void LCD_String(const char *msg);

void main() {
    TRISA = 0xFF;   // Set Port A as input for heartbeat sensor
    TRISB = 0x00;   // Set Port B as output for LCD
    LCD_Init();
    
    while (1) {
        unsigned int heartbeat = 0;
        for (int i = 0; i < 10; i++) { // Simple averaging filter
            heartbeat += (PORTA & 0x01); // Read heartbeat sensor on RA0
            __delay_ms(100);
        }
        heartbeat *= 6; // Convert to BPM
        
        LCD_Command(0x80);
        LCD_String("Heartbeat: ");
        char buffer[10];
        sprintf(buffer, "%d BPM", heartbeat);
        LCD_String(buffer);
        __delay_ms(500);
    }
}

// LCD Functions
void LCD_Command(unsigned char cmd) {
    PORTB = (cmd & 0xF0); RS = 0; EN = 1; __delay_ms(5); EN = 0;
    PORTB = ((cmd << 4) & 0xF0); RS = 0; EN = 1; __delay_ms(5); EN = 0;
}

void LCD_Char(unsigned char data) {
    PORTB = (data & 0xF0); RS = 1; EN = 1; __delay_ms(5); EN = 0;
    PORTB = ((data << 4) & 0xF0); RS = 1; EN = 1; __delay_ms(5); EN = 0;
}

void LCD_Init() {
    LCD_Command(0x02); // Initialize LCD in 4-bit mode
    LCD_Command(0x28);
    LCD_Command(0x0C);
    LCD_Command(0x06);
    LCD_Command(0x80);
}

void LCD_String(const char *msg) {
    while (*msg) {
        LCD_Char(*msg++);
    }
}
