/**
 * A program for an airline reservation management system.
 * Module 1 - Assignment 1, part 1
 * 
 * @author - Addie Domanico - CPSC 2710 - AO1
 * @version - 01/12/2024
 */

 import java.time.LocalDate;

public class SeatReservation {
    private String flightDesignator;
    private LocalDate flightDate;
    private String firstName;
    private String lastName;

    public String getFlightDesignator() {
        return flightDesignator;
    }

    public void setFlightDesignator(String flightDesignator) {
        this.flightDesignator = flightDesignator;
    }

    public LocalDate getFlightDate() {
        return flightDate;
    }

    public void setFlightDate(LocalDate date) {
        this.flightDate = date;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String fn) {
        this.firstName = fn;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String ln) {
        this.lastName = ln;
    }

    public String toString() {
        return "SeatReservation{" + "flightDesignator=" + flightDesignator + ", flightDate=" +
            flightDate + ", firstName=" + (firstName != null ? "\"" + firstName + "\"" : "null") +
            ", lastName=" + (lastName != null ? "\"" + lastName + "\"" : "null") + '}';
    }
}
