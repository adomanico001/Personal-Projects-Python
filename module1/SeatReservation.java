
/**
 * A program for an airline reservation management system.
 * Module 1 - Assignment 1
 * 
 * @author - Addie Domanico - CPSC 2710 - AO1
 * @version - 01/12/2024
 */

import java.time.LocalDate;

public class SeatReservation {
    // Instance variables
    private String flightDesignator;
<<<<<<< HEAD
    private LocalDate flightDate;
    private String firstName;
    private String lastName;
=======
    private java.time.LocalDate flightDate;
    private String firstName;
    private String lastName;
    private int numberOfBags;
    private boolean flyingWithInfant;
>>>>>>> 03e57147f642965c0e74606d100f7cd96e4bb51b

    // Getters and setters
    public String getFlightDesignator() {
        return flightDesignator;
    }

    public void setFlightDesignator(String flightDesignator) {
<<<<<<< HEAD
        if (flightDesignator.length() < 4 || flightDesignator.length() > 6) {
            throw new IllegalArgumentException("Flight Designator must have 4-6 characters.");
        }
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
=======
        if (flightDesignator == null) {
            throw new IllegalArgumentException("flight designator cannot be null");
        }

        if (flightDesignator.length() < 4 || flightDesignator.length() > 6) {
            throw new IllegalArgumentException("Flight designator must be 4-6 characters");
        }

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
    public int getNumberofBags() {
        return numberOfBags;
    }
    public void setNumberOfBags(int numberOfBags) {
        this.numberOfBags = numberOfBags;
    }
    public boolean isFlyingWithInfant() {
        return flyingWithInfant;
    }
    public void makeFlyingWithInfant() {
        this.flyingWithInfant = true;
    }
    public void makeNotFlyingWithInfant() {
        this.flyingWithInfant = false;
    }
    public String toString() {
        return String.format("SeatReservation{flightDesignator=%s, flightDate=%s, firstName=%s, lastName=%s}",
                flightDesignator, flightDate, firstName != null ? "\"" + firstName + "\"" : "null",
                lastName != null ? "\"" + lastName + "\"" : "null", numberOfBags, flyingWithInfant);
    }

}

    
>>>>>>> 03e57147f642965c0e74606d100f7cd96e4bb51b
