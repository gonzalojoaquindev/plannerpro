
export default function TwitterFollowCard({ children, formatUserName, userName, isFollowing }) {

    console.log(isFollowing)
    return (
        <article className='tw-followCard'>
            <header className='tw-followCard-header'>
                <img
                    className='tw-followCard-avatar'
                    src={`https://unavatar.io/twitter/${userName}`} />
                <div className='tw-followCard-info'>
                    <strong>{children}</strong>
                    <span className='tw-followCard-infoUserName' >{formatUserName(userName)}</span>
                </div>
            </header>
            <aside>
                <button className='tw-followCard-button'>Seguir</button>
            </aside>
        </article>
    )
}