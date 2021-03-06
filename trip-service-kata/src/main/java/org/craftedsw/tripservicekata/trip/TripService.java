package org.craftedsw.tripservicekata.trip;

import org.craftedsw.tripservicekata.exception.UserNotLoggedInException;
import org.craftedsw.tripservicekata.user.User;
import org.craftedsw.tripservicekata.user.UserSession;

import java.util.Collections;
import java.util.List;
import java.util.Optional;

public class TripService {

  private final TripDAO tripDAO;

  public TripService(TripDAO tripDAO) {

    this.tripDAO = tripDAO;
  }

  public List<Trip> getTripsByUser(User user) throws UserNotLoggedInException {

    User loggedUser = getLoggedUser().orElseThrow(() -> new UserNotLoggedInException());

    if (user.isFriend(loggedUser)) {
      return tripDAO.findTripsByUser(user); // why not user.trips() ??
    } else {
      return Collections.emptyList();
    }
  }

  protected Optional<User> getLoggedUser() {
    return Optional.ofNullable(UserSession.getInstance().getLoggedUser());
  }

}
