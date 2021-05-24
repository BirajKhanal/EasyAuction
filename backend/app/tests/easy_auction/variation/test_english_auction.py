from app.models.auction import AuctionSession, AuctionState, AuctionType
from sqlalchemy.orm import Session

from app.models.auction import Bid as BidModel
from app.tests.utils.auction import create_random_auction
from app.tests.utils.user import create_random_user
from app.easy_auction.auction_factory import auction_factory
from app.crud.auction.auction import crud_auction


def test_start_auction(db: Session):
    auction_db = create_random_auction(db)

    auction = auction_factory.get_auction(AuctionType.ENGLISH)

    auction.start(db, id=auction_db.id)
    db.refresh(auction_db)
    assert auction_db.session
    assert auction_db.session.state == AuctionState.ONGOING
    assert auction_db.session.bid_line == auction_db.starting_bid_amount
    assert auction_db.session.bid_cap == auction_db.bid_cap
    assert auction_db.session.reserve == auction_db.reserve


def test_end_auction(db: Session):
    auction_db = create_random_auction(db)

    auction = auction_factory.get_auction(AuctionType.ENGLISH)
    auction.start(db, id=auction_db.id)
    db.refresh(auction_db)
    assert auction_db.session.state == AuctionState.ONGOING
    auction.end(db, id=auction_db.id)
    db.refresh(auction_db)
    assert auction_db.session.state == AuctionState.ENDED


def test_bid_in_auction(db: Session):
    auction_db = create_random_auction(db)
    amount = auction_db.starting_bid_amount + 1
    bidder = create_random_user(db)

    auction = auction_factory.get_auction(AuctionType.ENGLISH)
    auction.start(db, auction_db.id)
    assert auction_db.session.state == AuctionState.ONGOING
    auction.bid(db, id=auction_db.id, amount=amount, bidder_id=bidder.id)

    auction_db = crud_auction.get(db, auction_db.id)
    assert auction_db.session.winning_bid
    winning_bid: BidModel = auction_db.session.winning_bid
    assert winning_bid.amount == amount
    assert winning_bid.bidder_id == bidder.id
    assert auction_db.session.last_bid_at
    assert auction_db.session.bid_line == amount + 1.25


def test_buy_it_now(db: Session):
    pass
