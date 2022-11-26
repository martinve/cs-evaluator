% rebase('base.tpl', title='Page Title')

<h1>Index</h1>

<table class="table table-hover">
    % for snt in sentences:
    <tr>
        <td>{{ snt.text }}</td>
        <td><a href="/sentences/{{ snt.id }}">Show</a></td>
    </tr>
    % end
</table>