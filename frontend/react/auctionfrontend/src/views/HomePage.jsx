import FeaturedList from "../components/FeaturedList"
import LiveAuction from "../components/LiveAuction"

const HomePage = () => {
    return (
        <div>
            <div className="container mt-2">
                <img src="https://dummyimage.com/1320x600/000/fff" class="img-fluid" alt="banner" />
            </div>
           <FeaturedList />
           <LiveAuction /> 
        </div>
    )
}

export default HomePage