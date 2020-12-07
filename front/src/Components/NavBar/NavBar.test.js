import React from 'react';
import renderer from 'react-test-renderer';
import {NavBar} from './NavBar.js';

test('Description generates correct page', () => {
    const component = renderer.create(
        <NavBar />
    );
    let tree = component.toJSON();
    expect(tree).toMatchSnapshot();
});
