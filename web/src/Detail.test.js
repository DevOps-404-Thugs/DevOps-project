import React from 'react';
import renderer from 'react-test-renderer';
import {Rating} from './Detail.js';

test('Rating generates correct starts without number of reviews', () => {
    const component = renderer.create(
        <Rating stars="3"/>
    );
    let tree = component.toJSON();
    expect(tree).toMatchSnapshot();
});

test('Rating generates correct starts 100 reviews', () => {
    const component = renderer.create(
        <Rating stars="3" numReviews="100"/>
    );
    let tree = component.toJSON();
    expect(tree).toMatchSnapshot();
});
