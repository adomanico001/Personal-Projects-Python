import static org.junit.Assert.assertEquals;

import java.time.LocalDate;
import org.junit.Test;

public class SeatReservationTest  {

  @Test
  public void canGetAndSetAllState() {
    SeatReservation sr = new SeatReservation();
    sr.setFirstName("Fred");
    sr.setLastName("Flintstone");
    LocalDate date = LocalDate.now();
    sr.setFlightDate(date);
    sr.setFlightDesignator("DL1331");
    assertEquals(sr.getFirstName(), "Fred");
    assertEquals(sr.getLastName(), "Flintstone");
    assertEquals(sr.getFlightDate(), date);
    assertEquals(sr.getFlightDesignator(), "DL1331");
  }

  /**
   * A flight designator with less than 4 characters is not allowed.  This test checks that
   * IllegalArgumentException is thrown when 3 character designator is provided.
   */
  @Test(expected = IllegalArgumentException.class)
  public void shortFlightDesignatorThrowsIllegalArgumentException() {
    SeatReservation sr = new SeatReservation();
    sr.setFlightDesignator("DL1");
  }

  /**
   * This test checks that IllegalArgumentException is thrown when a null flight designator is provided.
   */
  @Test(expected = IllegalArgumentException.class)
  public void nullFlightDesignatorThrowsIllegalArgumentException() {
    SeatReservation sr = new SeatReservation();
    sr.setFlightDesignator(null);
  }

  /**
   * A flight designator with more than 6 characters is not allowed.  This test checks that
   * IllegalArgumentException is thrown when a 7 character designator is provided.
   */
  @Test(expected = IllegalArgumentException.class)
  public void longFlightDesignatorThrowsIllegalArgumentException() {
    SeatReservation sr = new SeatReservation();
    sr.setFlightDesignator("DL1331a");
  }

  @Test
  public void toStringProducesCorrectStringWithAllNulls() {
    SeatReservation sr = new SeatReservation();
    assertEquals(sr.toString(),
        "SeatReservation{flightDesignator=null"+
        ",flightDate=null"+
        ",firstName=null"+
        ",lastName=null}");
  }

  @Test
  public void toStringProducesCorrectStringWithMixOfNulls() {
    SeatReservation sr = new SeatReservation();
    sr.setFirstName("Fred");
    sr.setLastName(null);
    LocalDate date = LocalDate.of(2023, 7, 30);
    sr.setFlightDate(date);
    sr.setFlightDesignator("DL1331");
    assertEquals(sr.toString(),
        "SeatReservation{flightDesignator=DL1331"+
            ",flightDate=2023-07-30"+
            ",firstName=Fred"+
            ",lastName=null}");
  }


  @Test
  public void toStringProducesCorrectStringWithNoNulls() {
    SeatReservation sr = new SeatReservation();
    sr.setFirstName("Fred");
    sr.setLastName("Flintstone");
    LocalDate date = LocalDate.of(2020, 3, 25);
    sr.setFlightDate(date);
    sr.setFlightDesignator("DL1331");
    assertEquals(sr.toString(),
        "SeatReservation{flightDesignator=DL1331"+
            ",flightDate=2020-03-25"+
            ",firstName=Fred"+
            ",lastName=Flintstone}");
  }
}
