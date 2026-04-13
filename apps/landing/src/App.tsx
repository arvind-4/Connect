import { useEffect } from 'react';
import { Route, Routes } from 'react-router-dom';

import Home from './pages/Home';

export default function App(): JSX.Element {
  useEffect(() => {
    (
      document.querySelector('html') as HTMLElement
    ).style.scrollBehavior = 'auto';
    window.scroll({ top: 0 });
    (
      document.querySelector('html') as HTMLElement
    ).style.scrollBehavior = '';
  }, []);

  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
}
