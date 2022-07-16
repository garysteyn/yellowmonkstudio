import navStyles from '../styles/Nav.module.css'

import Link from 'next/link'

function Nav() {
  return (
    <nav className={navStyles.nav}>
        <ul>
            <li>
                <Link href='/'>Home</Link>
            </li>
            <li>
                <Link href='/about'>About</Link>
            </li>
            <li>
                <Link href='explore'>Expore</Link>
            </li>
            <li>
                <Link href='/blog'>Blog</Link>
            </li>
            <li>
                <Link href='/contact'>Contact</Link>
            </li>
        </ul>
    </nav>
    )
}

export default Nav